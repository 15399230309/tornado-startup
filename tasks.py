from invoke import Collection

import startup.config
import startup.invoke.web as web

namespace = Collection()
namespace.configure({
    'project_root': startup.ROOT,
})

namespace.add_collection(Collection.from_module(web, name="web"))
