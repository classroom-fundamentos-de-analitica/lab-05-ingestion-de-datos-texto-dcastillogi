
import os

def get_phrases(folder_path, sentiment):
    phrases = []
    for file in os.listdir(f'{folder_path}/{sentiment}'):
        if not file.endswith('.txt'):
            continue
        with open(f'{folder_path}/{sentiment}/{file}', 'r', encoding='utf-8') as f:
            phrases.append(['"' + f.read().strip() + '"', '"' + sentiment + '"'])
    return phrases

def generate_file(folder_path, output_file):
    phrases = []

    # Open negative folder
    phrases.append(get_phrases(folder_path, 'negative'))

    # Open neutral folder
    phrases.append(get_phrases(folder_path, 'neutral'))

    # Open positive folder
    phrases.append(get_phrases(folder_path, 'positive'))

    # Write to file
    with open(output_file, 'w') as f:
        f.write('phrase,sentiment\n')
        for phrase_list in phrases:
            for phrase, sentiment in phrase_list:
                f.write(f'{phrase},{sentiment}\n')
        

generate_file('train', 'train_dataset.csv')
generate_file('test', 'test_dataset.csv')