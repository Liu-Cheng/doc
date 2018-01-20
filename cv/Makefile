TITLE=cv-ch
TEXORIG=cv-ch.tex

BIBFILES=
IMGFILES=
COMPILE=xelatex
#COMPILE=pdflatex

DOCX2TXT := docx2txt.pl

%.tex : %.docx
	$(DOCX2TXT) $< $@

$(TITLE).pdf : $(TEXORIG) $(BIBFILES) $(IMGFILES)
	$(COMPILE) $(TITLE)
#	bibtex $(TITLE)
	$(COMPILE) $(TITLE)
	$(COMPILE) $(TITLE)

.PHONY : clean
clean :
	\rm -f *~ *.log $(TITLE).pdf *.aux *.bbl *.blg *.lot *.lof
