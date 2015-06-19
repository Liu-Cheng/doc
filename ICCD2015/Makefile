TITLE=quickDough
TEXORIG=quickDough.tex abstract.tex introduction.tex framework.tex experiments.tex conclusions.tex relatedwork.tex

BIBFILES=refs.bib 
IMGFILES=

DOCX2TXT := docx2txt.pl

%.tex : %.docx
	$(DOCX2TXT) $< $@

$(TITLE).pdf : $(TEXORIG) $(BIBFILES) $(IMGFILES)
	pdflatex $(TITLE)
	bibtex $(TITLE)
	pdflatex $(TITLE)
	pdflatex $(TITLE)

.PHONY : clean
clean :
	\rm -f *~ *.log $(TITLE).pdf *.aux *.bbl *.blg *.lot *.lof
