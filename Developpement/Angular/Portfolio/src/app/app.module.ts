import { NgModule, CUSTOM_ELEMENTS_SCHEMA } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { MainComponent } from './main/main.component';
import { ErrorComponent } from './error/error.component';
import { HomeComponent } from './main/home/home.component';
import { HeaderComponent } from './main/header/header.component';
import { AboutComponent } from './main/about/about.component';
import { ContactComponent } from './main/contact/contact.component';
import { ProductItemComponent } from './_commons/components/product-item/product-item.component';
import { ContentAllProductsComponent } from './_commons/components/content-all-products/content-all-products.component';
import { ContentOneProductComponent } from './_commons/components/content-one-product/content-one-product.component';
import { OneProductComponent } from './main/one-product/one-product.component';
import { AllProductsComponent } from './main/all-products/all-products.component';

@NgModule({
  declarations: [
    AppComponent,
    MainComponent,
    ErrorComponent,
    HomeComponent,
    HeaderComponent,
    AboutComponent,
    ContactComponent,
    ProductItemComponent,
    ContentAllProductsComponent,
    ContentOneProductComponent,
    OneProductComponent,
    AllProductsComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    BrowserAnimationsModule,
  ],
  providers: [],
  bootstrap: [AppComponent],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
})
export class AppModule {}
