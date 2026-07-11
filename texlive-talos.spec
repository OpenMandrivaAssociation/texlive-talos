%global tl_name talos
%global tl_revision 61820

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A Greek cult font from the eighties
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/greek/talos
License:	gfl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/talos.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/talos.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A cult Greek font from the eighties, used at the University of Crete,
Greece. It belonged to the first TeX installation in a Greek University
and most probably the first TeX installation that supported the Greek
language.

