"""
This script generates a README.md file for a repository by listing the top-level directories and adding a license and contact section.

Created on Tue Non 7
Autor:     Enrique Rodriguez
"""

import os

# Get the directory of the current script
current_dir = os.path.dirname(os.path.realpath(__file__))

readme_folders = """
## Repository Structure
"""
  
for root, dirs, _ in os.walk(current_dir):
    level = root.replace(current_dir, '').count(os.sep)
    folder_name = os.path.basename(root)
    if level == 1 and folder_name not in ['.github', '.git', 'ChromeDriver']:  # Only process top-level directories and skip specified folders
        indent = ' ' * 4 * (level - 1)
        readme_folders += '{}- {}\n'.format(indent, folder_name)


readme_license = """
## License
Copyright 2023 Enrique Rodriguez

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

readme_welcome = """

# Welcome to Python Scripts

This are my best scripts i wrote in python for my daily work.

"""

readme_footer = """
## Contact
- [LinkedIn](https://www.linkedin.com/in/enrique-rodriguez-vela/)
- [Twitter](https://twitter.com/kikerodrivela)
- [GitHub](https://github.com/enriquetecfan11)
"""

readme_text = readme_welcome + readme_folders + readme_license + readme_footer

# Now you can write the generated text to your README file
with open('README.md', 'w') as f:
  f.write(readme_text)

print('README.md file generated')