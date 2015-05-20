var gulp = require('gulp');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var del = require('del');

var files = {
	'src': '*.js',
	'dist': 'dist/*.js'
};

gulp.task('clean', function (cb) {
	del('dist/', cb);
});

gulp.task('scripts', ['clean'], function () {
	return gulp.src(files.src)
		.pipe(concat('out.js'))
        .pipe(gulp.dest('dist/'));	
});

gulp.task('minify', ['scripts'], function () {
	return gulp.src(files.dist)
		.pipe(uglify('out.min.js'))
		.pipe(gulp.dest('dist/'));
});

gulp.task('build', ['minify']);

gulp.task('default', ['build']);