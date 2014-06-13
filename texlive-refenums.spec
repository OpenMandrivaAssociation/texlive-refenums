# revision 32562
# category Package
# catalog-ctan /macros/latex/contrib/refenums
# catalog-date 2014-01-03 20:50:16 +0100
# catalog-license lppl1.3
# catalog-version 1.1.1
Name:		texlive-refenums
Version:	1.1.1
Release:	2
Summary:	Define reference labels items with names of their own
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/refenums
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/refenums.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/refenums.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides commands to define enumerable items with a
number and a long name, which can be referenced referenced
later with the name or just the short form. For instance,
"Milestone M1: Specification created" can be defined and later
on be referenced with 'M1' or 'M1 ("Specification created")'.
The text in the references is derived from the definition and
also rendered as hyperlink to the definition.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/refenums/refenums.sty
%doc %{_texmfdistdir}/doc/latex/refenums/LICENSE
%doc %{_texmfdistdir}/doc/latex/refenums/README.md
%doc %{_texmfdistdir}/doc/latex/refenums/demo.pdf
%doc %{_texmfdistdir}/doc/latex/refenums/demo.tex
%doc %{_texmfdistdir}/doc/latex/refenums/test/demo-sec-param.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
