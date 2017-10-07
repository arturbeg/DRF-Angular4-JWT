import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpModule } from '@angular/http';

import { AppComponent } from './app.component';
import { UserComponent } from './components/user/user.component';
import { ConsumeRestAPIServices } from './services/consume-rest-api.service'

@NgModule({
  declarations: [
    AppComponent,
    UserComponent
  ],
  imports: [
    BrowserModule,HttpModule
  ],
  providers: [ConsumeRestAPIServices],
  bootstrap: [AppComponent]
})
export class AppModule { }
