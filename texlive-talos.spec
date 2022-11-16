Name:		texlive-talos
Version:	61820
Release:	1
Summary:	A Greek cult font from the eighties
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/talos
License:	gfl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/talos.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/talos.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A cult Greek font from the eighties, used at the University of
Crete, Greece. It belonged to the first TeX installation in a
Greek University and most probably the first TeX installation
that supported the Greek language.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/opentype/public/talos
%doc %{_texmfdistdir}/doc/fonts/talos

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
