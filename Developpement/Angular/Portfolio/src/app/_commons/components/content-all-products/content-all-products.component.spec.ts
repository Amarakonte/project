import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ContentAllProductsComponent } from './content-all-products.component';

describe('AllProductsComponent', () => {
  let component: ContentAllProductsComponent;
  let fixture: ComponentFixture<ContentAllProductsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ContentAllProductsComponent],
    }).compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ContentAllProductsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
