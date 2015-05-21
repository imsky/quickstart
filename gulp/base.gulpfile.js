/*
Basic Gulpfile from Quickstart
qkst.io/gulp/basic.js
*/
var gulp = require('gulp');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var del = require('del');

var paths = {
	'src': './',
	'dist': 'dist/'
};

var files = {
	'src': paths.src + '*.js',
	'dist': paths.dist + '*.js'
};

gulp.task('clean', function (cb) {
	del(paths.dist, cb);
});

gulp.task('scripts', ['clean'], function () {
	return gulp.src(files.src)
		.pipe(concat('bundle.js'))
        .pipe(gulp.dest(paths.dist));	
});

gulp.task('minify', ['scripts'], function () {
	return gulp.src(files.dist)
		.pipe(uglify('bundle.min.js'))
		.pipe(gulp.dest(paths.dist));
});

gulp.task('build', ['minify']);

gulp.task('default', ['build']);