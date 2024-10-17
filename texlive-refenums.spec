Name:		texlive-refenums
Version:	44131
Release:	2
Summary:	Define reference labels items with names of their own
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/refenums
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/refenums.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/refenums.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/refenums
%doc %{_texmfdistdir}/doc/latex/refenums

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
