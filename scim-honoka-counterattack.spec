%define version   0.0.1
%define release   %mkrel 6
%define src_name  honoka-coh

%define scim_honoka_version 0.8.2

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

Name:		scim-honoka-counterattack
Summary:	A mini-game for scim-honoka
Version:	%{version}
Release:	%{release}
Group:		Games/Other
License:	GPL
URL:		https://nop.net-p.org/modules/pukiwiki/index.php?%5B%5Bhonoka%2Fplugin%5D%5D
Source0:	%{src_name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:		%{libname} = %{version}
Requires:		scim-honoka >= %{scim_honoka_version}
BuildRequires:		scim-honoka-devel >= %{scim_honoka_version}
BuildRequires:		gettext-devel

%description
Scim-honoka-counterattack is a mini-game for scim-honoka to test the
timer feature.


%package -n %{libname}
Summary:	Scim-honoka-counterattack library
Group:		System/Internationalization
Provides:		%{libname_orig} = %{version}-%{release}

%description -n %{libname}
Scim-honoka-counterattack library.


%prep
%setup -q -n %{src_name}-%{version}

%build
# fix build (ut):
%define __libtoolize /bin/true

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std

# remove unnecessary files
rm -f %{buildroot}%{scim_plugins_dir}/honoka/*.{a,la}

%find_lang %{src_name}

%clean
rm -rf %{buildroot}

%files -f %{src_name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING

%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING
%{scim_plugins_dir}/honoka/*.so
