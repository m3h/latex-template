
.PHONY: FORCE_MAKE
# Taken from latexmk man pages
TARGETS = paper.pdf
DEPS_DIR = .deps
LATEXMK = latexmk -recorder -use-make -deps -f -interaction=batchmode \
	-e 'warn qq(In Makefile, turn off custom dependencies\n);' \
	-e '@cus_dep_list = ();' \
	-e 'show_cus_dep();'
all : $(TARGETS)
$(foreach file,$(TARGETS),$(eval -include $(DEPS_DIR)/$(file)P))
$(DEPS_DIR) :
	mkdir $@
%.pdf : %.tex FORCE_MAKE
	if [ ! -e $(DEPS_DIR) ]; then mkdir $(DEPS_DIR); fi
	$(LATEXMK) -deps-out=$(DEPS_DIR)/$@P $<

build/python/venv: build/python/venv/touchfile

build/python/venv/touchfile: src/python/requirements.txt
	test -d venv/venv || python -m venv build/python/venv
	. build/python/venv/bin/activate; \
		pip install \
		--upgrade \
		--requirement src/python/requirements.txt
	touch build/python/venv/touchfile

build/python/%.pgf : src/python/plots/%.py build/python/venv
	. ./build/python/venv/bin/activate; python $< $@

clean:
	rm -rf ./build/
