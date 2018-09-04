TITLE=main
TEXORIG=main.tex
IMGFILES=

DOCX2TXT := docx2txt.pl

%.tex : %.docx
	$(DOCX2TXT) $< $@

$(TITLE).pdf : $(TEXORIG) $(IMGFILES)
	xelatex $(TITLE)
	biber $(TITLE)
	xelatex $(TITLE)
	xelatex $(TITLE)

.PHONY : clean
clean :
	\rm -f *~ *.log $(TITLE).pdf *.aux *.bbl *.blg *.lot *.lof
