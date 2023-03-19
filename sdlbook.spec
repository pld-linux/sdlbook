%define		snap	20230319
Summary:	Simple djvu/pdf viewer
Summary(pl.UTF-8):	Prosta przeglądarka plików djvu i pdf
Name:		sdlbook
Version:	0.1
Release:	1.git%{snap}
License:	GPL v3
Group:		X11/Applications
Source0:	%{name}-%{snap}.tar.gz
# Source0-md5:	e19906bc00e765c3d1e730ac921a8e7e
URL:		https://github.com/rofl0r/SDLBook
BuildRequires:	SDL-devel
BuildRequires:	djvulibre-devel
BuildRequires:	mupdf-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tiny eBook reader using only SDL, djvulibre, and libmupdf.

%description -l pl.UTF-8
Mały czytnik ebooków korzystający tylko z SDL, djvulibre i
libmupdf.

%prep
%setup -q -n %{name}

%build
%{__make} \
	prefix=%{_prefix} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/sdlbook
