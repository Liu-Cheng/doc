TITLE=ppt-quickdough
FILES=ppt-quickdough.tex

BIBFILES=
IMGFILES=

#final : codes1078-so.tex
#	pdflatex codes1078-so
#	pdflatex codes1078-so

$(TITLE).pdf : $(FILES) $(BIBFILES) $(IMGFILES)
	pdflatex $(TITLE)
	pdflatex $(TITLE)
	bibtex $(TITLE)
	pdflatex $(TITLE)
	pdflatex $(TITLE)

.PHONY : clean
clean :
	\rm -f *~ *.log $(TITLE).pdf *.aux *.bbl *.blg *.lot *.lof
