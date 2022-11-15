Name:		texlive-cmexb
Version:	54074
Release:	1
Summary:	cmexb10 metrics and Type 1
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cmexb
License:	
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmexb.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmexb.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Computer Modern Math Extension bold, metrics and .pfb file.
Made by Petr Olsak via autotracing.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/type1/public/cmexb
%{_texmfdistdir}/fonts/tfm/public/cmexb
%{_texmfdistdir}/fonts/map/dvips/cmexb
%doc %{_texmfdistdir}/doc/fonts/cmexb

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
