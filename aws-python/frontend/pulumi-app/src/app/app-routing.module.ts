import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PartComponent} from './part/part.component';
import { DrawingComponent} from './drawing/drawing.component'
import { EcrComponent } from './ecr/ecr.component'

const routes: Routes = [
  {path: 'part',component: PartComponent},
  {path: 'drawing',component:DrawingComponent},
  {path: 'ecr',component:EcrComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
