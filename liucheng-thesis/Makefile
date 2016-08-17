TITLE=liucheng-thesis
TEXORIG=liucheng-thesis.tex acknowledgement.tex cover.tex abstract.tex front-page.tex chapter1-intro.tex chapter2-litrev.tex chapter4-framework.tex chapter3-overlay.tex chapter5-customization.tex chapter6-conclusion.tex appendix.tex

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
