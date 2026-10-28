from pydantic import BaseModel, Field, computed_field,field_validator
from typing import Annotated, Literal




class OutputResponse(BaseModel):
    predicted_catgeory: Annotated[str, Field(...,title='result')]
    confidence: Annotated[float, Field(..., gt=0, title='Confidence score')]
    class_proabilites: Annotated[dict[str,float], Field(..., title='Class wise proability')]
    

   