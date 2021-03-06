/*
Gulpfile (Babel + Webpack) from Quickstart
qkst.io/js/gulpfile-babel-webpack
*/

// npm install --save-dev gulp webpack-stream babel-loader

var gulp = require('gulp');
var webpack = require('webpack-stream');

gulp.task('transpile', function() {
  return gulp.src('index.js')
    .pipe(webpack({
      output: {
        library: 'Library',
        filename: 'library.js',
        libraryTarget: 'umd'
      },
      module: {
        loaders: [{
          loader: 'babel-loader'
        }]
      }
    }))
    .pipe(gulp.dest('./dist'));
});

gulp.task('default', ['transpile']);