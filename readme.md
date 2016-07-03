### Multilingual python

Attempt to make the scratch-python transition more accessile to kids. It takes a dictionary with keyword translations, applies it to a modified python Grammar file and generates a new Grammar file that accepts the translated keywords as valid

#### Usage

To translate a grammar file: 
* Make sure the language you want is in the languages file
* run `python translate.py [language]`
* Copy the generated `grammar_[language]` file to the Grammar folder in your python source folder, overwriting the `Grammar` file
* Compile python as usual
* The compiled python binary should accept the translated keywords

To contribute with a new translation:
* Modify the template.py file and add your translations in the empty strings
* Change the dict name for the language, and the file for `[language].py` (ASCII only)
* Add that file to the languages folder and make a pull request

#### Catches

* This only translates python expressions, not the functions in the standard library
