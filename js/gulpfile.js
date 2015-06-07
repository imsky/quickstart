/*
Base Gulpfile from Quickstart
qkst.io/js/gulpfile
*/

// npm install --save-dev gulp gulp-concat gulp-uglify gulp-rename del

var gulp = require('gulp');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');
var del = require('del');
var path = require('path');

var paths = {
  'src': './',
  'dist': './dist'
};

var files = {
  'src': [
    path.join(paths.src, '*.js'),
    '!node_modules/',
    '!bower_components/'
    ],
  'dist': path.join(paths.dist, '*.js')
};

gulp.task('clean', function (cb) {
  del(paths.dist, cb);
});

gulp.task('bundle', ['clean'], function () {
  return gulp.src(files.src, {
      'base': './'
    })
    .pipe(concat('bundle.js'))
    .pipe(gulp.dest(paths.dist)); 
});

gulp.task('minify', ['bundle'], function () {
  return gulp.src(files.dist, {
      'base': './'
    })
    .pipe(rename({
      'dirname': '',
      'extname': '.js',
      'suffix': '.min'
    }))
    .pipe(uglify())
    .pipe(gulp.dest(paths.dist));
});

gulp.task('default', ['minify']);
