# file-header-injector
Prepends file header for a filetype to a file in order to bypass filetype checks
# Usage
To show a list of supported/known filetypes use `injector.py list`.
The syntax for "changing" filetypes of a given file is as follows:
`injectory.py file extension`
For example:
`injector.py somefile.php jpg`
A new file "somefile.php.jpg" will be created. `file somefile.php.jpg` will return `testfile.php.jpg: JPEG image data`.
