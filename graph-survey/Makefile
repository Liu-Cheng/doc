TITLE=report
FILES=report.tex \
	  litrev-2016-09-13.tex \
	  litrev-2016-09-20.tex \
	  litrev-2016-10-06.tex \
	  litrev-2016-10-13.tex \
	  litrev-2016-10-20.tex \
	  litrev-2016-10-27.tex \
	  litrev-2016-11-03.tex \
	  litrev-2016-11-17.tex \
	  litrev-2016-12-08.tex

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
