# gulp-python-example
This repository provides a Gulp task file containing developer tools for Python

## Installation
At first, clone this repository to the location of your choice. Then install required dependencies by:
```sh
sudo apt-get install python-pip nodejs graphviz
sudo pip install pylint autopep8 clonedigger pycallgraph coverage sphinx vulture nose
sudo npm install gulp -g
```

After having installed the dependencies, please go to cloned folder and install the Nodejs dependencies:
```sh
sudo npm install
```

Now you can start report and documentation tasks by the following command (See gulp.js for included tasks):
```sh
gulp
```

## Note
Work on this repository is still in progress. Further documentation will occur soon.