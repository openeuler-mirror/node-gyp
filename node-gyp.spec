%{?nodejs_find_provides_and_requires}
Name:                node-gyp
Version:             3.6.0
Release:             4
Summary:             Node.js native addon build tool
License:             MIT
URL:                 https://github.com/nodejs/node-gyp
Source0:             https://github.com/nodejs/node-gyp/archive/v%{version}/node-gyp-%{version}.tar.gz
Source1:             addon-rpm.gypi
Patch1:              node-gyp-addon-gypi.patch
Patch2:              node-gyp-system-gyp.patch
Patch3:              node-gyp-python.patch
Patch4:              node-gyp-python3.patch
Patch5:              node-gyp-node12.patch
BuildArch:           noarch
ExclusiveArch:       %{nodejs_arches} noarch
Requires:            gyp nodejs-devel libuv-devel http-parser-devel gcc-c++
BuildRequires:       gyp nodejs-devel libuv-devel http-parser-devel gcc-c++
BuildRequires:       npm(tape) npm(bindings) npm(fstream) npm(glob) npm(graceful-fs) npm(minimatch)
BuildRequires:       npm(mkdirp) npm(nan) >= 2.0.0 npm(nopt) npm(npmlog) npm(osenv) npm(path-array)
BuildRequires:       npm(request) npm(require-inject) npm(rimraf) npm(semver) npm(tar) npm(which) vim
%description
node-gyp is a cross-platform command-line tool written in Node.js for compiling
native addon modules for Node.js, which takes away the pain of dealing with the
various differences in build platforms. It is the replacement to the node-waf
program which is removed for node v0.8.

%prep
%autosetup -p1
cp -p %{SOURCE1} addon-rpm.gypi
%nodejs_fixdep glob "^6.0.4"
%nodejs_fixdep minimatch "^3.0.0"
rm -rf gyp

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/node-gyp
cp -pr addon*.gypi bin lib package.json %{buildroot}%{nodejs_sitelib}/node-gyp
mkdir -p %{buildroot}%{_bindir}
ln -sf ../lib/node_modules/node-gyp/bin/node-gyp.js %{buildroot}%{_bindir}/node-gyp
%nodejs_symlink_deps

%check
%{nodejs_symlink_deps} --check
%{nodejs_sitelib}/tape/bin/tape test/test-*.js

%files
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/node-gyp
%{_bindir}/node-gyp

%changelog
* Thu Jan 21 2021 lingsheng <lingsheng@huawei.com> - 3.6.0-4
- Limit npm(nan) version to fix test errors

* Tue Dec 29 2020 huanghaitao <huanghaitao8@huawei.com> - 3.6.0-3
- Fix test errors in node 12+

* Tue Sep 15 2020 chengzihan <chengzihan2@huawei.com> - 3.6.0-2
- add patch node-gyp-python3.patch
- default to python3 instead of python2

* Mon Aug 17 2020 Shaoqiang Kang <kangshaoqiang1@huawei.com> - 3.6.0-1
- Package init
