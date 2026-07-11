%global tl_name cmexb
%global tl_revision 54074

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	cmexb10 metrics and Type 1
Group:		Publishing
URL:		https://www.ctan.org/pkg/cmexb
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmexb.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cmexb.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Computer Modern Math Extension bold, metrics and .pfb file. Made by Petr
Olsak via autotracing.

