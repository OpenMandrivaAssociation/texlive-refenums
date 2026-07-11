%global tl_name refenums
%global tl_revision 44131

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1.2
Release:	%{tl_revision}.1
Summary:	Define named items and provide back-references with that name
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/refenums
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/refenums.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/refenums.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides commands to define enumerable items with a number
and a long name, which can be referenced later with the name or just the
short form. For instance, "Milestone M1: Specification created" can be
defined and later on be referenced with 'M1' or 'M1 ("Specification
created")'. The text in the references is derived from the definition
and also rendered as hyperlink to the definition.

