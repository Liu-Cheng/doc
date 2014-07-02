TITLE=benchmark
FILES=benchmark.tex 
BIBFILES=fpt_refs.bib 
IMGFILES=

#final : codes1078-so.tex
#	pdflatex codes1078-so
#	pdflatex codes1078-so

$(TITLE).pdf : $(FILES) $(BIBFILES) $(IMGFILES)
	xelatex $(TITLE)
	bibtex $(TITLE)
	xelatex $(TITLE)
	xelatex $(TITLE)

.PHONY : clean
clean :
	\rm -f *~ *.log $(TITLE).pdf *.aux *.bbl *.blg *.lot *.lof
