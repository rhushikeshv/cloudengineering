import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { PartComponent } from './part/part.component';
import { DrawingComponent } from './drawing/drawing.component';
import { EcrComponent } from './ecr/ecr.component';

@NgModule({
  declarations: [
    AppComponent,
    PartComponent,
    DrawingComponent,
    EcrComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
