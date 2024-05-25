import nbformat as nbf

def md_to_ipynb(md_file, ipynb_file):
    # Read the markdown content
    with open(md_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # Create a new notebook
    nb = nbf.v4.new_notebook()

    buffer = []
    in_code_block = False
    
    for line in lines:
        line_stripped = line.strip()
        if line_stripped.startswith("```"):  # Detect start or end of a code block
            if in_code_block:  # Ending a code block
                # Add the buffer as a code cell
                code = "".join(buffer).strip()
                if code:  # Only add non-empty code cells
                    nb['cells'].append(nbf.v4.new_code_cell(code))
                buffer = []
                in_code_block = False
            else:  # Starting a code block
                # Add the buffer as a markdown cell
                md = "".join(buffer).strip()
                if md:  # Only add non-empty markdown cells
                    nb['cells'].append(nbf.v4.new_markdown_cell(md))
                buffer = []
                in_code_block = True
        else:
            buffer.append(line)

    # Handle any remaining content in the buffer
    content = "".join(buffer).strip()
    if content:
        if in_code_block:
            nb['cells'].append(nbf.v4.new_code_cell(content))
        else:
            nb['cells'].append(nbf.v4.new_markdown_cell(content))

    # Write the notebook to a file
    with open(ipynb_file, 'w', encoding='utf-8') as f:
        nbf.write(nb, f)

# Provide your input .md file and desired output .ipynb file
md_path = './numpy/solutions/100_Numpy_exercises_solutions.md'
ipynb_path = './numpy/solutions/100_Numpy_exercises_solutions.ipynb'
md_to_ipynb(md_path, ipynb_path)