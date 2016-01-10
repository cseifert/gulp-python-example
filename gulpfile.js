var gulp = require('gulp'),
	shell = require('gulp-shell'),
	runSequence = require('run-sequence');

var config = {
	sourceDir: 'project/',
	reportDir: 'reports/',
	docDir: 'docs/',
	testDir: 'test/'
};

/**
 * Creates missing directories
 */
gulp.task('prepare', shell.task(
	[
		'mkdir -p ' + config.reportDir,
		'mkdir -p ' + config.docDir
	]
));

/**
 * Runs pylint on all python files within the project directory
 */
gulp.task('pylint', function() {
    var files = [];

    gulp.src(config.sourceDir + '**/*.py')
        .on('data', function(file) {
            files.push(file.path);
        })
        .on('data', function() {
            shell.task(
				['pylint ' + files.join(' ') + ' -f html > ' + config.reportDir + 'pylint_report.html'],
				{quiet: true, ignoreErrors: true}
			)();
        });
});

/**
 * Runs autopep8 to automatically fix PEP8 issues
 */
gulp.task('autopep8', function() {
    var files = [];

    gulp.src(config.sourceDir + '**/*.py')
        .on('data', function(file) {
            files.push(file.path);
        })
        .on('data', function() {
            shell.task(['autopep8 --in-place --recursive --aggressive --aggressive ' + files.join(' ')])();
        });
});

/**
 * Runs the clonedigger command to find duplicate code
 */
gulp.task('clonedigger', shell.task(
	['clonedigger ' + config.sourceDir + ' --ignore-dir=' + config.testDir +
	' --output ' + config.reportDir + 'clonedigger.html'
	]
));

/**
 * Runs pycallgraph on all python files to generate diagrams showing the call graphs
 */
gulp.task('pycallgraph', function() {
    var files = [];

    gulp.src([config.sourceDir + '**/*.py', '!/**/__init__.py', '!' + config.sourceDir + config.testDir + '*'])
        .on('data', function(file) {
            files.push(file.path);
        })
        .on('data', function() {
            shell.task([
					'cd ' + config.sourceDir +
					' && pycallgraph graphviz --output-file ' + __dirname + '/' + config.reportDir + 'pycallgraph.png' +
					' -- ' + files.join(' ')
				],
				{quiet: true}
			)();
        });
});

/**
 * Runs coverage on all python files to generate a code coverage report
 */
gulp.task('coverage', function() {
    var files = [];

    gulp.src([config.sourceDir + '**/*.py', '!/**/__init__.py', '!' + config.sourceDir + config.testDir + '*'])
        .on('data', function(file) {
            files.push(file.path);
        })
        .on('data', function() {
            shell.task([
				'cd ' + config.sourceDir +
				' && coverage run ' + files.join(' ') +
				' && coverage html',
				'mv ' + config.sourceDir + 'htmlcov ' + __dirname + '/' + config.reportDir + 'htmlcov',
				'rm ' + config.sourceDir + '.coverage'
			],
			{quiet: true, ignoreErrors: true}
			)();
        });
});

/**
 * Runs pyreverse on all python files to generate UML diagrams of the packages and classes
 */
gulp.task('pyreverse', function() {
    var directories = [];

    gulp.src([config.sourceDir + '**/*.py', '!/**/__init__.py', '!' + config.sourceDir + config.testDir + '*'])
        .on('data', function(file) {
			reduced_file = file.path.replace(__dirname + '/' + config.sourceDir, '');

			if (reduced_file.indexOf('/') === -1) {
				directories.push(reduced_file);
			} else {
				folder = reduced_file.replace(/[^\/]*$\//, '')

				if (directories.indexOf(folder) === -1) {
					directories.push(folder);
				}
			}
        })
        .on('data', function() {
            shell.task([
				'cd ' + config.sourceDir + ' && pyreverse -o png -p Uml ' + directories.join(' '),
				'mv ' + config.sourceDir + '*.png ' + config.docDir
				],
				{quiet: true, ignoreErrors: true}
			)();
        });
});

/**
 * Runs the sphinx command to create an automated API documentation
 */
gulp.task('sphinx', shell.task(
	[
		'sphinx-apidoc ' + config.sourceDir + ' -o ' + config.docDir + 'sphinx/source --force',
		'cd ' + config.docDir + 'sphinx && make clean && make html'
	]
));

/**
 * Runs the vulture command to find unused code without executing the module
 */
gulp.task('vulture', shell.task(
	[
		'vulture ' + config.sourceDir + ' --exclude=' + config.sourceDir + config.testDir +
		' | tee ' + config.reportDir + 'vulture.txt'
	],
	{ignoreErrors: true}
));

/**
 * Runs nosetests to run unit tests
 */
gulp.task('test', shell.task(
	['nosetests ' + config.sourceDir + ' -v 2>&1 | tee ' + config.reportDir + 'unittests.txt']
));

/**
 * Report task to bundle single reporting tasks
 */
gulp.task('report', function(callback){
	runSequence('prepare', 'pylint', 'clonedigger', 'pycallgraph', 'coverage', 'vulture', 'test', callback)
});

/**
 * Documentation task to bundle single documentation tasks
 */
gulp.task('documentate', function(callback){
	runSequence('prepare', 'sphinx', 'pyreverse', callback)
});

/**
 * Default gulp task to run reports and documentation
 */
gulp.task('default', function(callback){
	runSequence('documentate', 'report', callback)
});