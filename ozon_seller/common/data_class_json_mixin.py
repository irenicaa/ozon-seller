import dataclasses_json


class DataClassJsonMixin(dataclasses_json.DataClassJsonMixin):
    dataclass_json_config = dataclasses_json.config( # type: ignore[assignment]
        undefined=dataclasses_json.Undefined.EXCLUDE,
    )["dataclasses_json"]
