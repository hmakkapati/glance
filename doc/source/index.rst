..
      Copyright 2010 OpenStack Foundation
      All Rights Reserved.

      Licensed under the Apache License, Version 2.0 (the "License"); you may
      not use this file except in compliance with the License. You may obtain
      a copy of the License at

          http://www.apache.org/licenses/LICENSE-2.0

      Unless required by applicable law or agreed to in writing, software
      distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
      WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
      License for the specific language governing permissions and limitations
      under the License.

==================================
Welcome to Glance's documentation!
==================================

The Image service (glance) project provides a service where users can upload
and discover data assets that are meant to be used with other services.
This currently includes images and metadata definitions.

Glance image services include discovering, registering, and
retrieving virtual machine (VM) images. Glance has a RESTful API that allows
querying of VM image metadata as well as retrieval of the actual image.

.. include:: deprecation-note.inc

VM images made available through Glance can be stored in a variety of
locations from simple filesystems to object-storage systems like the
OpenStack Swift project.

To learn how to contribute to Glance, see:

.. toctree::
   :maxdepth: 2

   contributing/index

Ocata
~~~~~

To install Glance, see the Ocata Image service install guide for each distribution:

- `Ubuntu <https://docs.openstack.org/ocata/install-guide-ubuntu/glance.html>`_
- `CentOS and RHEL <https://docs.openstack.org/ocata/install-guide-rdo/glance.html>`_
- `openSUSE and SUSE Linux Enterprise <https://docs.openstack.org/ocata/install-guide-obs/glance.html>`_

Newton
~~~~~~

To install Glance, see the Ocata Image service install guide for each distribution:

- `Ubuntu <https://docs.openstack.org/newton/install-guide-ubuntu/glance.html>`_
- `CentOS and RHEL <https://docs.openstack.org/newton/install-guide-rdo/glance.html>`_
- `openSUSE and SUSE Linux Enterprise <https://docs.openstack.org/newton/install-guide-obs/glance.html>`_

Developer reference
~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2

   architecture
   database_architecture
   database_migrations
   domain_model
   domain_implementation

User guide
~~~~~~~~~~

.. TODO - move this content to docs.o.o

.. toctree::
   :maxdepth: 2

   identifiers
   statuses
   formats
   common-image-properties
   metadefs-concepts
   glanceapi
   glanceclient
   glancemetadefcatalogapi
   signature
   api/modules

Administration guide
~~~~~~~~~~~~~~~~~~~~

.. TODO - move this content to docs.o.o

.. toctree::
   :maxdepth: 2

   tasks
   configuring
   sample-configuration
   authentication
   policies
   flows
   property-protections
   opts/index
   requirements

Operating Glance
~~~~~~~~~~~~~~~~

.. TODO - move this content to docs.o.o

.. toctree::
   :maxdepth: 1

   controllingservers
   db
   rollingupgrades
   cache
   notifications


