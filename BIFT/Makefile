TITLE=book
TEXORIG=book.tex acknowledgement.tex chapter2.tex chapter4.tex chapter6.tex foreword.tex part.tex acronym.tex chapter1.tex chapter3.tex chapter5.tex dedication.tex glossary.tex preface.tex 

BIBFILES=refs.bib 
IMGFILES=

CH1=chapter1
CH2=chapter2
CH3=chapter3
CH4=chapter4
CH5=chapter5
CH6=chapter6
DOCX2TXT := docx2txt.pl

%.tex : %.docx
	$(DOCX2TXT) $< $@

$(TITLE).pdf : $(TEXORIG) $(BIBFILES) $(IMGFILES)
	pdflatex $(TITLE)
	bibtex $(CH1)
	bibtex $(CH2)
	bibtex $(CH3)
	bibtex $(CH4)
	bibtex $(CH5)
	pdflatex $(TITLE)
	pdflatex $(TITLE)

.PHONY : clean
clean :
	\rm -f *~ *.log $(TITLE).pdf *.aux *.bbl *.blg *.lot *.lof
