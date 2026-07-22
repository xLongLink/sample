from longlink import Router
from src.envs import env
from src.resources import fs
from src.types.user import UserModel
from src.services.sample import sample

router = Router()


@router.get("/sample", response_model=dict[str, str])
async def sample_get_endpoint():
    """Handle sample GET request."""

    filesystem = fs
    return {
        "message": "Sample GET endpoint received data",
        "required": env.REQUIRED,
        "optional": env.OPTIONAL,
        "filesystem_protocol": str(filesystem.protocol),
        "filesystem_type": type(filesystem).__name__,
    }


@router.post("/sample", response_model=UserModel)
async def sample_post_endpoint():
    """Create a sample record and return a typed payload."""

    return await sample.create_project()
