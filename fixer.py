import re

# limit = 100

# with open("generated_dataset.txt", "r") as f1, open("generated_dataset_clean.txt", "a") as t2:
#     for line in f1:
#         if (limit > 0):
#             s = re.split(r'([.!?]+)', line.strip())
#             print(s)
#             limit -= 1


def process_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf8') as infile:
        lines = infile.readlines()

    modified_lines = []
    
    for i in range(len(lines) - 1):  # Loop through lines except the last one
        line = lines[i].strip()
        next_line = lines[i + 1].strip()
        
        # Define a regular expression to match sentences ending with "!", ".", or "?"
        sentence_end_pattern = r'([^.?!]*[.?!])'
        
        # Extract the last sentence from the current line and the first sentence from the next line
        last_sentences_current_line = re.findall(sentence_end_pattern, line)#[-1].strip()
        first_sentence_next_line = re.findall(sentence_end_pattern, next_line)[0].strip()

        k = False
        # Check if the sentences match
        for l in last_sentences_current_line:
            l = l.strip()
            if first_sentence_next_line == l:
                # Replace the space before the repeated part with a tab
                new_line = re.sub(r'\s+' + re.escape(l), '\t' + l, line).lower()
                new_line = new_line.replace("’", "'")
                new_line = new_line.replace("—", ", ")
                new_line = new_line.replace("\"", "")
                modified_lines.append(new_line)
                k = True
        if not k:
            line = line.lower()
            line = line.replace("’", "'")
            line = line.replace("—", ", ")
            line = line.replace("\"", "")
            modified_lines.append(line)

    # Handle the last line which doesn't have a next line to compare to
    modified_lines.append(lines[-1].strip())

    # Write the modified lines to the output file
    with open(output_file, 'w', encoding='utf8') as outfile:
        outfile.write("\n".join(modified_lines))


input_file = 'generated_dataset.txt'
output_file = 'generated_dataset_clean.txt'
process_lines(input_file, output_file)
