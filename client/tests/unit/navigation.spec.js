import { expect } from "chai";
import { shallowMount } from "@vue/test-utils";
import Navigation from "@/components/HelloWorld.vue";

describe("HelloWorld.vue", () => {
  it("renders props.msg when passed", () => {
    const msg = "new message";
    const wrapper = shallowMount(Navigation, {
      props: { msg },
    });
    expect(wrapper.text()).to.include(msg);
  });
});
