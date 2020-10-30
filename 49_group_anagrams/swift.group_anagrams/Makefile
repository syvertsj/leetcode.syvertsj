
SHELL = /bin/bash -O extglob
SC = swiftc
FLG = -v 

.PHONY: clean start 

start:
	@echo "make [<filename>|clean]"

%: %.swift
	@$(SC) $(FLG) $<

clean:
	@rm -f !(*.swift|Makefile*)

