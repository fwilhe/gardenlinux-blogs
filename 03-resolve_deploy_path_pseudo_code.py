def ostree_kernel_parameter():
    return "/ostree/boot.0/osname/HASH/0"


def realpath(path):
    return path.replace("//", "/")


def stat(path):
    return True


def resolve_deploy_path(root_mountpoint="/sysroot"):
    ostree_target = ostree_kernel_parameter()
    # ostree_target = /ostree/boot.N/osname/HASH/0
    destpath = f"{root_mountpoint}/{ostree_target}"
    # destpath = /sysroot//ostree/boot.N/osname/HASH/0
    deploy_path = realpath(destpath)
    if not stat(deploy_path):
        raise Exception(f"Deploy path {deploy_path} does not exist")
    # deploy_path = /sysroot/ostree/boot.N/osname/HASH/0
    return deploy_path
