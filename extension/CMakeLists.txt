cmake_minimum_required(VERSION 3.10)
project(fake-extension)

# PostgreSQL 17 包
install(FILES fake.control fake--1.0.sql
        DESTINATION /usr/share/postgresql/17/extension
        COMPONENT postgresql-17)

# PostgreSQL 18 包
install(FILES fake.control fake--1.0.sql
        DESTINATION /usr/share/postgresql/18/extension
        COMPONENT postgresql-18)

set(CPACK_PACKAGE_CONTACT "sanbei101 <sanbei101@outlook.com>")
set(CPACK_DEBIAN_PACKAGE_MAINTAINER "sanbei101 <sanbei101@outlook.com>")

set(CPACK_COMPONENT_POSTGRESQL-17_DISPLAY_NAME "PostgreSQL 17 Fake Extension")
set(CPACK_COMPONENT_POSTGRESQL-17_DESCRIPTION "Fake data generator for PostgreSQL 17")
set(CPACK_DEBIAN_POSTGRESQL-17_PACKAGE_NAME "postgresql-17-fake-extension")
set(CPACK_DEBIAN_POSTGRESQL-17_PACKAGE_DEPENDS "postgresql-17")

set(CPACK_COMPONENT_POSTGRESQL-18_DISPLAY_NAME "PostgreSQL 18 Fake Extension")  
set(CPACK_COMPONENT_POSTGRESQL-18_DESCRIPTION "Fake data generator for PostgreSQL 18")
set(CPACK_DEBIAN_POSTGRESQL-18_PACKAGE_NAME "postgresql-18-fake-extension")
set(CPACK_DEBIAN_POSTGRESQL-18_PACKAGE_DEPENDS "postgresql-18")

set(CPACK_DEB_COMPONENT_INSTALL ON)
set(CPACK_GENERATOR "DEB")

include(CPack)