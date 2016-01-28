/*
 * Sample test code
 *
 */

import org.junit.Test;
import org.junit.Assert;

public class HelloWorldTests
{
	@Test
	public void testReturnHelloWorldString() {
		String actual = HelloWorld.returnHelloWorldString();
		String expected = HelloWorld.HELLO_WORLD;

		Assert.assertTrue( 
			"expected \"" + expected + "\", but got \"" + actual + "\"instead",
			actual == expected);
	}
}
