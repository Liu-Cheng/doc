TITLE=main
TEXORIG=main.tex chapter.tex quickdough.tex

BIBFILES=literature.bib 
IMGFILES=alu-v2.pdf dfg-gen.pdf overlay_overview.pdf pe.pdf qd_overlay.pdf qd_overview.pdf quickdough_framework.pdf scgra-accelerator.pdf qd_customization_ex.pdf qd_customization_resource.pdf

DBDIR=/Users/skhay/Dropbox/FSP_Book/7_0_Overlays
DBTEX=$(addprefix $(DBDIR)/,$(TEXORIG))
DBIMG=$(addprefix $(DBDIR)/figs/,$(IMGFILES))

DOCX2TXT := docx2txt.pl

%.tex : %.docx
	$(DOCX2TXT) $< $@

$(TITLE).pdf : $(TEXORIG) $(BIBFILES)
	pdflatex $(TITLE)
	bibtex $(TITLE)
	pdflatex $(TITLE)
	pdflatex $(TITLE)

.PHONY : clean upload
clean :
	\rm -f *~ *.log $(TITLE).pdf *.aux *.bbl *.blg *.lot *.lof

upload : $(DBTEX) $(DBDIR)/literature.bib $(DBIMG)

$(DBDIR)/%.tex : %.tex
	cp $< $(DBDIR)/

$(DBDIR)/literature.bib : literature.bib
	cp $< $(DBDIR)/

$(DBDIR)/figs/%.pdf : figs/%.pdf
	cp $< $(DBDIR)/figs/
