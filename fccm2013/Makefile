TITLE=hlsMethodology
FILES=hlsMethodology.tex abstract.tex introduction.tex results.tex conclusions.tex methodology.tex scgra.tex related.tex

BIBFILES=refs.bib 
IMGFILES=

#final : codes1078-so.tex
#	pdflatex codes1078-so
#	pdflatex codes1078-so

$(TITLE).pdf : $(FILES) $(BIBFILES) $(IMGFILES)
	pdflatex $(TITLE)
	bibtex $(TITLE)
	pdflatex $(TITLE)
	pdflatex $(TITLE)

.PHONY : clean
clean :
	\rm -f *~ *.log $(TITLE).pdf *.aux *.bbl *.blg *.lot *.lof
