const gulp = require('gulp'),
      sass = require('gulp-sass')(require('sass')),
      cssnano = require('gulp-cssnano'), 
      rename = require('gulp-rename'); 

gulp.task('sass', function () { 
	return gulp.src('../scss/**/*.scss') 
		.pipe(sass())
		.pipe(cssnano())
		.pipe(rename({suffix: '.min'}))
		.pipe(gulp.dest('../css')) 
});

gulp.task('watch', function() {
	gulp.watch('../scss/**/*.scss', gulp.parallel('sass'));
});

gulp.task('default', gulp.parallel('sass', 'watch'));