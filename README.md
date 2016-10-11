<!--
http://www.apache.org/licenses/LICENSE-2.0.txt


Copyright 2015 Intel Corporation

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
-->
# snap pytest (spytest)

Module for writing large tests (integration tests) for [snap](http://github.com/intelsdi-x/snap) plugins.

1. [Documentation](#documentation)
2. [License](#license-and-authors)
3. [Acknowledgements](#acknowledgements)

## Documentation

Setting up binaries
-------------------------------------------------------------------------------------------

The `bins` package provides objects like:

- `Binaries` for agregation
- `Snapd` to interact with Snap daemon binary
- `Snapctl` to interact with snapctl binary
- `Plugin` to handle plugin binaries

```python
    # set and download required binaries (snapd, snapctl, plugins)
    binaries = bins.Binaries()
    binaries.snapd = bins.Snapd(snapd_url, snap_dir)
    binaries.snapctl = bins.Snapctl(snapctl_url, snap_dir)
    binaries.collector = bins.Plugin(psutil_url, plugins_dir, "collector", 7)
    binaries.processor = bins.Plugin(passthru_url, plugins_dir, "processor", -1)
    binaries.publisher = bins.Plugin(mockfile_url, plugins_dir, "publisher", -1)
```

Download binaries
-------------------------------------------------------------------------------------------

```python
    utils.download_binaries(binaries)
```

Start snapd
-------------------------------------------------------------------------------------------

```python
    binaries.snapd.start()
        if not binaries.snapd.isAlive():
            fail("snapd thread died")
```

Interact with snapctl
---------------------

```python
    # load all plugins
    for plugin in binaries.get_all_plugins():
        loaded = binaries.snapctl.load_plugin(plugin)
            
    # check available metrics, plugins and tasks
    metrics = binaries.snapctl.list_metrics()
    plugins = binaries.snapctl.list_plugins()
    tasks = binaries.snapctl.list_tasks()
```


## License
Snap, along with this module, is an Open Source software released under the Apache 2.0 [License](LICENSE.txt).

## Acknowledgements

* Author: [Marcin Krolik](https://github.com/marcin-krolik)
