###############################################################################
## Makefile for rus-morph
###############################################################################

RELEASE=0.1
VERSION=0.1.0
LANG1=rus
BASENAME=apertium-$(LANG1)

TARGETS_COMMON = $(LANG1)_guesser.automorf.hfst $(LANG1)_guesser.automorf.bin
	# $(LANG1).automorf.bin $(LANG1).autogen.bin \
	# $(LANG1).autopgen.bin \
	# $(LANG1).automorf.bin $(LANG1)_guesser.automorf.bin $(LANG1).autogen.bin \
	# $(LANG1).automorf.att.gz $(LANG1).autogen.att.gz \
	# $(LANG1).automorf.hfst $(LANG1).autogen.hfst

# if HAVE_VISLCG3
# TARGETS_COMMON += $(LANG1).rlx.bin
# endif # HAVE_VISLCG3


#	$(LANG1).autopgen.bin


all: $(LANG1).lexc
	cat $(LANG1).lexc > all.$(LANG1).lexc
	echo "LEXICON Nouns" >> all.$(LANG1).lexc
	cat lexc/roots.lexc >> all.$(LANG1).lexc
	# cat lexc/roots_k.lexc >> all.$(LANG1).lexc
	# cat lexc/roots_ost.lexc >> all.$(LANG1).lexc
	# cat lexc/roots_a_ija.lexc >> all.$(LANG1).lexc
	cat lexc/morphoids.lexc >> all.$(LANG1).lexc
	cat lexc/roots.lexc >> all.$(LANG1).lexc
	# cat lexc/roots_k.lexc >> all.$(LANG1).lexc
	# cat lexc/roots_ost.lexc >> all.$(LANG1).lexc
	# cat lexc/roots_a_ija.lexc >> all.$(LANG1).lexc
	# --Werror
	hfst-lexc all.$(LANG1).lexc -o $(LANG1).lexc.hfst
	hfst-fst2fst --format=optimized-lookup-weighted -i $(LANG1).lexc.hfst -o $(LANG1).hfstol



## Guesser

guesser.hfst: $(LANG1).guesser.hfst
	echo "" | hfst-xfst -e "source $<" -e "save stack $@" -e "quit"

$(LANG1)_guesser.lexc.hfst: $(LANG1).lexc.hfst guesser.hfst
	hfst-substitute -i $(LANG1).lexc.hfst -o $@ -f '{🂡}:{🂡}' -T guesser.hfst

restrict_guesser.hfst: $(LANG1).restrict_guesser.hfst
	hfst-regexp2fst $< -o $@

$(LANG1)_guesser.automorf.hfst: $(LANG1)_guesser.lexc.hfst restrict_guesser.hfst
	cat $(LANG1)_guesser.lexc.hfst | hfst-invert | hfst-compose -1 - -2 restrict_guesser.hfst | hfst-invert | hfst-fst2fst -O -o $@
# .deps/$(LANG1)_guesser.hfst: .deps/$(LANG1)_guesser.lexc.hfst .deps/$(LANG1).twol.hfst
# 	hfst-compose-intersect -1 .deps/$(LANG1)_guesser.lexc.hfst -2 .deps/$(LANG1).twol.hfst -o $@
#
# $(LANG1)_guesser.automorf.hfst: .deps/$(LANG1)_guesser.hfst .deps/spellrelax.hfst .deps/restrict_guesser.hfst .deps/cjk.hfst
# 	cat .deps/$(LANG1)_guesser.hfst | hfst-invert | hfst-compose -1 - -2 .deps/restrict_guesser.hfst | hfst-invert | hfst-compose-intersect -1 - -2 .deps/spellrelax.hfst | hfst-substitute -f '{乚}:{乚}' -T .deps/cjk.hfst | hfst-invert | hfst-fst2fst -O -o $@
#
# $(LANG1)_guesser.automorf.bin: $(LANG1)_guesser.automorf.hfst .deps/.d
# 	hfst-fst2txt $(LANG1)_guesser.automorf.hfst   > .deps/$(LANG1)_guesser.autogen.att
# 	lt-comp lr .deps/$(LANG1)_guesser.autogen.att $@

clear:
	rm guesser.hfst $(LANG1)_guesser.lexc.hfst restrict_guesser.hfst $(LANG1)_guesser.automorf.hfst $(LANG1).lexc.hfst $(LANG1).hfstol
