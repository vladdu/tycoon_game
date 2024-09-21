tailor:
	@pants tailor --check update-build-files --check ::
all: 
	@pants update-build-files
	@pants fmt lint check test package ::
