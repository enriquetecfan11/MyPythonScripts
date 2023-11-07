"""
Created on Tue Non 7
Autor:     Enrique Rodriguez
"""

import os

def generate_readme(path):
    readme_text = """
    # Welcome to Python Scripts

    This are my best scripts i wrote in python for my daily work.

    ## License
    Copyright 2017 ChenQi

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
    
    ## Repository Structure
    """
    
    for root, dirs, _ in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        if level == 1:  # Only process top-level directories
            indent = ' ' * 4 * (level - 1)
            readme_text += '{}- {}\n'.format(indent, os.path.basename(root))
    return readme_text

# Get the directory of the current script
current_dir = os.path.dirname(os.path.realpath(__file__))

readme_text = generate_readme(current_dir)

# Now you can write the generated text to your README file
with open('README.md', 'w') as f:
    f.write(readme_text)